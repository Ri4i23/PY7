import Contacts
import Contact
def MainFunction():
    command = input(("Введите 1 , если вы хотите просмотреть список контактов\n"
           "Введите 2 , если вы хотите добавить в список контактов\n"))
    if command =="1":
        Contacts.ShowMeContactList()
    elif command =="2":
        Contact.AddContactInContactList()
    else:
        print("Вы осуществили неправильный ввод. Перезапустите и введите нормально!")