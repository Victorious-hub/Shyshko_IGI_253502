from apps.affiliates.enums import ContractType
from apps.users.models import Affiliate, Agent, Feedback
from apps.users.utils import get_object
from .models import Answer, Company, Contract, Coupon, InsuranceType, News, Policy, Vacancy
from django.db.models import Q

def vacancy_list() -> Vacancy:
    obj = Vacancy.objects.all()
    return obj

def feedback_list() -> Feedback:
    obj = Feedback.objects.all()
    return obj

def affiliate_list() -> Affiliate:
    obj = Affiliate.objects.all()
    return obj

def get_company_detail() -> Company:
    return Company.objects.all()

def list_affiliate_employee(affiliate_id: int) -> Agent:
    obj = Agent.objects.filter(affiliate__id=affiliate_id)
    return obj

def news_list() -> News:
    obj = News.objects.all()
    return obj

def incurance_list() -> InsuranceType:
    return InsuranceType.objects.all()

def get_client_contracts(id: int) -> Contract:
    agent = get_object(Agent, user__id=id)
    contracts: Contract = Contract.objects.filter(
        Q(affiliate=agent.affiliate) & 
        Q(status=ContractType.SIGNED.value)).order_by('client__user__email')
    return contracts

def get_contracts(id: int) -> Contract:
    contracts = Contract.objects.filter(client__user__id=id)
    return contracts

def get_client_contract(id: int) -> Contract:
    contract = get_object(Contract, id=id)
    return contract

def get_client_policy(id: int) -> Policy:
    policy = Policy.objects.filter(contract__id=id).first()
    return policy

def list_active_coupons() -> Coupon:
    return Coupon.objects.all()

def get_answer(id: int) -> Answer:
    return Answer.objects.get(id=id)

def list_news() -> News:
    return News.objects.all()

def get_news(id: int) -> News:
    return News.objects.get(id=id)