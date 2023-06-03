from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculator(request):
    # return HttpResponse("계산기 기능 구현")
    
    
    # 1. 데이터 확인 
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    operators=request.GET.get('operators')
    
    # 2. 계산
    if operators =='+':
        result = num1 + num2
    elif operators =='-':
        result = num1 - num2
    elif operators =='*':
        result = num1 * num2
    elif operators =='/':
        result = num1 / num2
    else: #방어 코딩 => 방어적 프로그래밍(Defensive programming)은 예상치 못한 입력에도 한 소프트웨어가 계속적 기능 수행을 보장할 수 있도록 고안된 방어적 설계의 한 형태이다. 
        result = 0
    
    # 3. 응답    
    return render(request, 'calculator.html')