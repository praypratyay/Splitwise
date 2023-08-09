# Design Splitwise (Low Level Design)

## **OVERVIEW**

> Splitwise is an application where different users form groups to maintain and settle their expenses.

<p>
    <img src="splitwise.jpg" width="800" height="500" />
</p>

We dont want just entities for this. We want to build an entire software system thats takes input via commandline. Persist data in a real database.
I will be using Django for this.

## Requirements (Already Provided)

- Users can register and update their profiles

- A user's profile should contain at least their name, phone number and 

- Users can participate in expenses with other users

- Users can participate in groups.

- To add an expense, a user must specify either the group, or the other users involved in the expense, along with who paid
  what and who owes what. They must also specify a description for the expense.

- A user can see their total owed amount

- A user can see a history of the expenses they're involved in

- A user can see a history of the expenses made in a group that they're participating in

- Users shouldn't be able to query about groups they are not a member of

- Only the user who has created a group can add/remove members to the group

- Users can request a settle-up. The application should show a list of transactions, which when executed will ensure that
  the user no longer owes or recieves money from any other user. Note that this need not settle-up any other users.

- Users can request a settle-up for any group they're participating in. The application should show a list of transactions, which if executed, will ensure that everyone participating in the group is settled up (owes a net of 0 Rs). Note that will only deal with the expenses made inside that group. Expenses outside the group need not be settled.

- When settling a group, we should try to minimize the number of transactions that the group members should make to
  settle up.

## Input Format

### Register vinsmokesanji 003 namisswwaann
> u1 is registering with the username "vinsmokesanji", phone "003" and password as "namisswwaann"
-- --

### u1 UpdateProfile robinchwan
> u1 is updating their profile password to "robinchwan"
-- --

### u1 AddGroup Roommates
> u1 is creating a group titled "Roommates"
-- --

### u1 AddMember g1 u2
> u1 is adding u2 as a member of the group "Roommates" (which has the id g1)
-- --

### u1 MyTotal
> u1 is asking to see the total amount they owe/recieve after everything is settled.
-- --

### u1 History
> u1 is asking to see their history of transactions (whether added by themselves or someone
else)
-- --

### u1 Groups
> u1 is asking to see the groups that they're a member of
-- --

### u1 SettleUp
> u1 is asking to see the list of transactions they should perform to settle up
-- --

### u1 SettleUp g1
> u1 is asking to see the list of transactions that need to be performed by members of g1 to
completely settle up the group.
-- --

### u1 Expense g1 iPay 1000 Equal Desc Wifi Bill
> u1 is adding an expense in the group g1.
> u1 paid 1000 Rs
> each user of g1 owes an equal amount (the exact amount will depend on the number of users in group g1. Say g1 has 5
users, then the amount owed by each will be 200 Rs.
-- --

### u1 Expense u2 u3 u4 iPay 1000 Equal Desc Last night dinner
> u1 is adding an expense with users u2, u3 and u4.
> u1 paid 1000 Rs
> each user owes an equal amount - 250 Rs.
-- --

### u1 Expense u2 u3 iPay 1000 Percent 20 30 50 Desc House rent
> u1 is adding an expense with users u2 and u3
> u1 paid 1000 Rs
> u1 owes 20% (200 Rs), u2 owes 30% (300 Rs) and u3 owes 50% (500 Rs).
-- --

### u1 Expense u2 u3 u4 iPay 1000 Ratio 1 2 3 4 Desc Goa trip
> u1 is adding an expense with users u2, u3 and u4.
> u1 paid 1000 Rs
> u1 owes 100 Rs (1 part), u2 owes 200 Rs (2 parts), u3 owes 300 Rs (3 parts) and u4 owes 400 Rs (4
parts).
-- --

### u1 Expense u2 u3 iPay 1000 Exact 100 300 600 Desc Groceries
> u1 is adding an expense with users u2 and u3.
> u1 paid 1000 Rs
> u1 owes 100 Rs, u2 owes 300 Rs and u3 owes 600 Rs.
-- --

### u1 Expense u2 u3 MultiPay 100 300 200 Equal Desc Lunch at office
> u1 is adding an expense with users u2 and u3.
> u1 paid 100 Rs, u2 paid 300 Rs and u3 paid 200 Rs.
> Each user owes an equal amount - 200 Rs.
-- --

### u1 Expense u2 u3 MultiPay 500 300 200 Percent 20 30 50 Desc Netflix subscription
> u1 is adding an expense with users u2 and u3.
> u1 paid 500 Rs, u2 paid 300 Rs and u3 paid 200 Rs.
> u1 owes 20% (200 Rs), u2 owes 30% (300 Rs) and u3 owes 50% (500 Rs).

Note -  I am going to update Django Command Interface to use these commands after tweaking them a little bit.

## Clarifications

**Q) Does the user need to be registered to include them in an expense?**
> _No. We can include a user even if they are not registered._

**Q) u1 can add an expense what other users?**
> - _either from a group - g1_
> - _or specific people - u2 u3 u4_

**Q) Who pays for the expense?**
> - _iPay amount_
> - _MultiPay a1 a2 a3_

**Q) What can be the division of expenses?**
> - _equal_
> - _by percentage_
> - _by ratio_
> - _exact amount_

Note: Make the reasonable assumptions 100/3 = 33.33 assign one person 33.34 and the rest 33.33

## Notes

### How to SettleUp?

- We have a list of expenses.
- We compute how much extra/less every user paid.
- Now we have to find list of transactions :
   - **Algo 1:** Arrange users in a list, every user settles themselves with the next person which is not an intuitive way. _[n people can settle in n-1 transactions]_
   - **Algo 2:** Divide the users into two buckets, one who have paid more and the other who has paid less. While both buckets are not empty, take any one user out from each bucket and make a transaction of min(|A|,|B|) from lesser user to more user, and update the value of more user. This is intuitive since anyone who has paid more will not be asked to pay again and vice versa. _[n people can settle in n-1 transactions]_

## Classes - Attributes - Interfaces

### User
- ID
- Name
- PhoneNumber
- Email
- Password
- Status
- Groups (list of Group)

### Group
- ID
- Description
- CreatedBy 
- Members (list of User)

### Expense
- ID
- Description
- Amount
- Type
- CreatedBy
- Group
- Users

### UserStatus
- ACTIVE/INVITED

### ExpenseType
- EXPENSE/TRANSACTION

### UserExpense (Mapping Class)
- User
- Expense
- Share
- UserExpenseType

### UserExpenseType
- PAID/HADTOPAY

## Schema Design (TABLES)

### User
| `ID` | `Name` | `PhoneNumber` | `Password` | `UserStatusID` 
| --- | --- | --- | --- | --- 
| xx | xx | xx | xx | xx 

### Group
| `ID` | `Description` | `CreatedByUserID` 
| --- |  --- | --- 
| xx |  xx | xx 

### Expense
| `ID` | `Description` | `Amount` | `ExpenseTypeID` | `CreatedByUserID` | `GroupID`
| --- | --- | --- | --- | --- | ---
| xx | xx | xx | xx | xx | xx

### UserExpense
| `UserID`  | `ExpenseID` | `Share` | `UserExpenseTypeID`
| --- | --- | --- | --- 
| xx | xx | xx | xx 

### UserGroup
| `UserID` | `GroupID` 
| --- | --- 
| xx | xx 

### UserStatus
| `ID` | `Value`  
| --- | --- 
| xx | xx 

### ExpenseType
| `ID` | `Value`  
| --- | --- 
| xx | xx 

### UserExpenseType
| `ID` | `Value`  
| --- | --- 
| xx | xx 

## HOW TO RUN?

```python 
python3 manage.py migrate
python3 manage.py runserver 5555
```