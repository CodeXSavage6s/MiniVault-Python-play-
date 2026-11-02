import json
import os
import uuid

FILE_NAME = "notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Notes file contains invalid JSON.")
        return []

def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)

def add_note(notes):
    text = input("Enter your note: ").strip()

    if not text:
        print("Note cannot be empty.")
        return

    note = {
        "id": str(uuid.uuid4()),
        "text": text
    }

    notes.append(note)
    save_notes(notes)

    print("Note saved successfully!")

def list_notes(notes):
    if not notes:
        print("No notes saved yet.")
        return

    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Note: {note['text']}")

def delete_notes(notes):
    if not notes:
      print("No note to delete")
      return 

    print("\n--- Delete a Note ---")

    for n, note in enumerate(notes, start=1):
    
      print(f"\n{n}.   ID: {note['id']}")
      print(f"     Note: {note['text']}")

    choice = input("\nEnter the number of the note you want to delete (or press Enter to cancel): ").strip()

    try: 
      index = int(choice)
      if 1 <= index <= len(notes):
        deleted = notes.pop(index - 1)
        save_notes(notes)
        print(f"\nNote No. {index} deleted successfully")
      else:
        print("\nNumber not valid, Please try again")
        
    except ValueError:
      print("\nPlease Enter Valide Number") 
      return

def edit_notes(notes):
    if not notes:
      print("No note found")
      return 

    print("\nEdit Notes")

    for n, note in enumerate(notes, start=1):
      print(f"\n{n}.   ID: {note['id']}")
      print(f"     Note: {note['text']}")

    choice = input("Select note to edit: ")

    try:
      index = int(choice)
      if 1 <= index <= len(notes):
        note = input("Edit selected note: ").strip()

        if not note:
          print("Note cannot be empty ")
          return
          
        notes[index-1]["text"] = note
        save_notes(notes)
        print(f"Edited Note No.{index} successfully")
      else:
        print("Input not valid, please try again")
    except ValueError:
      print("Enter a valid number")  

def main():
    notes = load_notes()

    while True:
        print("\n=== MiniVault ===")
        print("1. Add note")
        print("2. List no(tes")
        print("3. Delete from list")
        print("4. Edit from list")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            delete_notes(notes)
        elif choice == "4":
            edit_notes(notes)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
