import json
from dataclasses import dataclass, asdict

list1 = []


@dataclass
class User:
    name: str
    phone: str
    age: int
    gender: str

    @staticmethod
    def submit(user_str):
        data = asdict(user_str)
        list1.append(data)
        data = json.dumps(list1)

        try:
            f = open('data.txt', 'w')
        except FileNotFoundError:
            return False

        f.write(data)
        f.close()
        return True


@dataclass
class Bank(User):
    balance: int = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Updated Account Balance is: $", self.balance)


def view_balance(phone):
    try:
        with open('data.txt', 'r') as f:
            temp = json.load(f)
            for entry in temp:
                if entry["phone"] == phone:
                    print("Account Balance is: $", entry['balance'])
                    break
                else:
                    return

    except FileNotFoundError:
        print('file not found')
        return

    f.close()


def exist(phone, file_name):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('file data.txt not found, please retry')
        return False

    temp = f.readlines()
    for i in temp:
        if phone in i:
            f.close()
            return True
    f.close()
    return False


def update(phone, amount):
    try:
        with open('data.txt', 'r') as f:
            user_details = json.load(f)
            newlist = []
            for each in user_details:
                if phone == each['phone']:
                    newRecord = {}
                    newRecord['name'] = each['name']
                    newRecord['phone'] = each['phone']
                    newRecord['age'] = each['age']
                    newRecord['gender'] = each['gender']
                    new_Amount = each['balance'] + amount
                    if (new_Amount < 0):
                        print("Insufficient Fund ")
                        newRecord['balance'] = each['balance']
                    else:
                        newRecord['balance'] = new_Amount
                    print("Updated Account Balance is: $", newRecord['balance'])
                    newlist.append(newRecord)
                else:
                    newRecord = {}
                    newRecord['name'] = each['name']
                    newRecord['phone'] = each['phone']
                    newRecord['age'] = each['age']
                    newRecord['gender'] = each['gender']
                    newRecord['balance'] = each['balance']
                    newlist.append(newRecord)
                with open('data.txt', 'w') as file:
                    file.write(json.dumps(newlist))

    except FileNotFoundError:
        print('file not found')
        return

    f.close()


def display_user_data(file_name):
    try:
        with open(file_name, 'r') as f:
            temp = json.load(f)
            print("{}\t {}\t\t {} {}\t".format('Name', 'Phone', 'Age', 'Balance'))
            for i in temp:
                print("{}\t {}\t {}\t {}\t ".format(i['name'], i['phone'], i['age'], i['balance']))
    except FileNotFoundError:
        print('file not found')
        return

    f.close()



def delete_user(data, file_name):
    try:
        with open(file_name, 'r') as f:
            temp = json.load(f)
    except FileNotFoundError:
        print('file not found')
        return False
    f.close()

    for i in temp:
        if data == i['phone']:
            temp.remove(i)
    try:
        with open(file_name, 'w') as file:
            file.write(json.dumps(temp))
    except FileNotFoundError:
        print('something went wrong')
        return False

    f.close()
    return True


while True:
    print(' 1 Open Account\n 2 Deposit Money\n 3 View Account Balance\n 4 Admin login\n 5 Withdraw Money\n 6.quit')

    try:
        choice = int(input())
    except TypeError:
        print('looks like you did not enter an integer')
        continue
    except ValueError:
        print('Invalid key entered')
    else:
        if choice == 1:
            user_name = input('enter your name ')
            user_name = user_name.strip()
            while True:
                phone = input('enter your Phone Number')
                if exist(phone, 'data.txt'):
                    print('Account already exist with this number')
                    continue
                else:
                    break
            while True:
                try:
                    print('Enter your age ')
                    age = int(input())
                except (TypeError, ValueError):
                    print('Age should be number')
                    continue
                else:
                    break

            while True:
                print("Enter your gender 'm' male\t 'f' female\t 'o' others ")
                gender = input()
                if gender in 'mMfFoO':
                    break
                else:
                    print('please enter only mentioned characters')
                    continue
            user = Bank(user_name, phone, age, gender)
            success = user.submit(user)
            if success:
                print("Account Opened Successfully")
            else:
                print("Something went wrong,Try again")


        elif choice == 2:

            phone = input('enter your phone no. ')
            phone = phone.strip()
            if not exist(phone, 'data.txt'):
                print('Account not found')
            else:
                while True:
                    try:
                        money = int(input('enter the amount of money to be Deposited '))
                    except ValueError:
                        print('money should be in number')
                        continue
                    else:
                        break
                update(phone, money)

        elif choice == 3:
            phone = input('enter your phone ')
            phone = phone.strip()
            if exist(phone, 'data.txt'):
                view_balance(phone)
            else:
                print('Account does not exist')


        elif choice == 4:
            password = input('enter password ').strip()
            if not exist(password, 'admin.txt'):
                print("password doesn't match")
                continue
            else:
                while True:
                    print("1 check user's data\t 2 delete user\t 3 logout")
                    try:
                        admin_choice = int(input())
                    except TypeError:
                        print('looks like you did not enter an integer')
                        continue
                    except ValueError:
                        print('Invalid key entered')
                    else:
                        if admin_choice == 1:
                            display_user_data('data.txt')
                        elif admin_choice == 2:
                            phone = input('enter phone of the user you want to delete ').strip()
                            if exist(phone, 'data.txt'):
                                if delete_user(phone, 'data.txt'):
                                    print('user deleted successfully')
                                else:
                                    print('unable to delete user data')
                            else:
                                print("user with the given Phone Number doesn't exists")
                        elif admin_choice == 3:
                            break
                        else:
                            print('invalid choice')
                break

        elif choice == 5:
            phone = input('enter your phone no. ')
            phone = phone.strip()
            if not exist(phone, 'data.txt'):
                print('Account not found')
            else:
                while True:
                    try:
                        money = 0 - int(input('enter the amount of money to be Debited'))
                    except ValueError:
                        print('money should be in number')
                        continue
                    else:
                        break
                update(phone, money)

        elif choice == 6:
            break
        else:
            print('invalid choice!')
