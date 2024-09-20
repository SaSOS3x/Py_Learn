import Person
import PersonBalance

sasha = Person.Person("Sasha", 20)

sasha_balance = PersonBalance.PersonBalance(sasha)

sasha_balance.earn(1000, True)
sasha_balance.earn(1500, False)

sasha_balance.pay(200, True)
sasha_balance.pay(500, True)
sasha_balance.pay(1000, False)
sasha_balance.pay(1000, True)