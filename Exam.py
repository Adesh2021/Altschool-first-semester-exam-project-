from datetime import datetime
import uuid
class Expense:
     def __init__(self,title,amount) :
          self.id=str(uuid.uuid4())
          self.title=title
          self.amount=float(amount)
          self.created_at=datetime.utcnow()
          self.updated_at=self.created_at

def updated_at(self,title=None,amount=None):
     if title is not None:
         self.title=title
         if amount is not None:
             self.amount=amount
             self.updated_at=datetime.utcnow()

     def to_dict(self):
          return{"id":self.id,"title":self.title,"amount":self.amount,"created_at":self.created_at.isoformat(),"updated":self.update.isofromat()}


class ExpensesDatbase:
    def __init__(self):
          self.expenses=[]
def add_expense(self,expense):
         self.expenses.append(expense)
def remove_expense(self,expense_id):
         self.expenses=[x for x in self.expenses if x.id != expense_id]
def get_expense_by_id(self,expense_id):
         for expense in self.expenses:
           if expense.id==expense_id:
            return expense
           return None
def get_expenses_title(self,title):
         return [expense for expense in self.expenses if expense.title==title]
def to_dict(self):
         return[expense.to_dict() for expense in self.expenses]



           

          