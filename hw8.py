shopping_bag={}
def buy(shopping_bag):
    print('[구입]')
    while True:
        item=str(input('상품명?'))
        if item=='':
            return False
        num=int(input('수량은?'))
        shopping_bag[item]=num
        print(f'장바구니에 {item} {num}개가 담겼습니다.')
def show(shopping_bag):
    print(f'>>> 장바구니 보기:{shopping_bag}')
def find(shopping_bag):
    print('[검색]')
    Q=str(input('장바구니에서 확인하고자 하는 상품은?'))
    if Q in shopping_bag:
        print(f'{Q}은(는) {shopping_bag.get(Q)}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {Q}(은)는 없습니다.')
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)