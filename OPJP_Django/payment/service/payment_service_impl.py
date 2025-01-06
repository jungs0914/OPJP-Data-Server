from kakao_account.entity.account import Account
from kakao_account.repository.account_repository_impl import AccountRepositoryImpl
from payment.entity.payment import Payment
from payment.repository.payment_repository_impl import PaymentRepositoryImpl
from payment.service.payment_service import PaymentService
from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl


class PaymentServiceImpl(PaymentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__paymentRepository = PaymentRepositoryImpl.getInstance()
            cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    # def paymentRegister(self, paymentData, accountId):
    #     account = self.__accountRepository.findById(accountId)
    #     paymentData = self.__paymentRepository.findById(account)
    #     if paymentData is None:
    #         print("구독권 새로 구입")
    #         paymentData = self.__paymentRepository.register(account)
    #     else:
    #         print("기존 구독권 사용")
        
    #     paymentId = paymentData.get('paymentId')
    #     print(f"paymentId:", {paymentId})

    #     accountId = paymentData.get('accountId')
    #     print(f"accountId:", {accountId})

    #     subscriptionId = paymentData.get('subscriptionId')
    #     print(f"subscriptionId:", {subscriptionId})

    #     paymentItemList = self.__paymentRepository.findAllByPaymentId(paymentId)
    #     print(f"paymentItemList:", {paymentItemList})

    #     paymentItem = None
    #     for item in paymentItemList:
    #         paymentFromSubscriptionItem = item.payment
    #         accountFromPayment = paymentFromSubscriptionItem.account
    #         if accountFromPayment.id == account.id:
    #             paymentItem = item
    #             break
        
    #     if paymentItem is None:
    #         print("신규 구독권 신청")
    #         subscription = self.__subscriptionRepository.findBySubscriptionId(subscriptionId)
    #         self.__paymentRepository.register(paymentData, subscription)
    #     else:
    #         print("기존 구독권 사용")
    #         self.__paymentItemRepository.update(paymentItem)
    
    # def paymentList(self, accountId):
    #     account = self.accountRepository.findById(accountId)
    #     subscription = self.__subscriptionRepository.findByAccount(account)
    #     print(f"paymentList -> subscription: {subscription}")
    #     subscriptionItemList = self.__subscriptionItemRepository.findByPayment(subscription)
    #     print(f"paymentList -> paymentItemList: {subscriptionItemList}")
    #     paymentItemListResponseForm = []

    #     for paymentItem in paymentItemList:
    #         paymentItemResponseForm = {
    #             'paymentId': paymentItem.paymentId,
    #             'account': paymentItem.account,
    #             'subscription': paymentItem.subscription,
    #         }
    #         paymentItemListResponseForm.append(paymentItemResponseForm)
        
    #     return paymentItemListResponseForm
    
    # def removePaymentItem(self, paymentItemId):
    #     return self.__paymentItemRepository.deleteByPaymentItemId(paymentItemId)

    def process(self, accountId, paymentKey, orderId, amount):
        try:
            print(f"accountId: {accountId}")
            account = self.__accountRepository.findById(accountId)

            paymentRequestData = {
                "paymentKey": paymentKey,
                "orderId": orderId,
                "amount": amount,
            }
            print(
                f"paymentRepositoryData: {paymentRequestData}"
            )

            # 결제 요청을 레퍼지토리로 넘기고 결과 받기
            paymentResult = self.__paymentRepository.request(paymentRequestData)
            print(
                f"paymentResult: {paymentResult}"
            )

            if paymentResult:
                # 결제 정보를 DB에 저장
                payment = Payment(
                    account=account,
                    payment_key=paymentKey,
                    order_id=orderId,
                    amount=amount,
                    provider=paymentResult.get('easyPay', {}).get('provider'),
                    method=paymentResult.get('method'),
                    paid_at=paymentResult.get('approvedAt'),
                    receipt_url=paymentResult.get('receipt', {}).get('url'),
                )
                self.__paymentRepository.create(payment)    # 결제 정보 DB에 저장

                return paymentResult
            else:
                raise Exception("결제 요청 처리 실패")
            
            
        except Exception as e:
            print(f"결제 처리 중 오류 발생: {e}")
            return {
                "error": "Internal server error",
                "success": False,
            }, 500