# -*- coding: utf-8 -*-

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Görev eklendi:", task)

    def show_tasks(self):
        if self.tasks:
            print("Yapılacaklar Listesi:")
            for idx, task in enumerate(self.tasks, start=1):
                print("%d %s " % (idx, task))
        else:
            print("Yapılacak görev yok.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print("Tamamlanan görev:", completed_task)
        else:
            print("Geçersiz görev numarası.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevleri Göster")
        print("3. Görev Tamamlandı")
        print("4. Çıkış\n")
        choice = input("\nSeçiminizi yapın: ")

        if choice == "1":
            task = input("\nYeni görevi girin: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            todo_list.show_tasks()
            task_index = int(input("\nTamamlanan görevin numarasını girin: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Çıkıyor...\n")
            break
        else:
            print("Geçersiz seçenek.")

if __name__ == "__main__":
    main()
