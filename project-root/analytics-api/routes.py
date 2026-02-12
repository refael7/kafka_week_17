from fastapi import APIRouter
from dal import top_10_customers
route = APIRouter()


@route.get('/analytics/top-customers')
def top_customers():
    return top_10_customers()


@route.get('/analytics/customers-without-orders')
def top_customers():
    return


@route.get('/analytics/zero-credit-active-customers')
def top_customers():
    return