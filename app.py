import pywhatkit
import datetime
import time
from threading import Thread

# List of contacts (initial list)
contacts = {
    '1': '+919545883002',
    '2': '+917498157771',
    '3': '+918208805916'
}

# Function to send WhatsApp message
def send_whatsapp_message(num, message, delay_time):
    # Get current time
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute + 2  # Adding a 2-minute buffer for the message time

    # Adjust if minutes exceed 60
    if current_minute >= 60:
        current_minute -= 60
        current_hour += 1

    # Send message via pywhatkit
    try:
        pywhatkit.sendwhatmsg(num, message, current_hour, current_minute, wait_time=10)
        print(f"Message scheduled to {num} at {current_hour}:{current_minute}")
    except Exception as e:
        print(f"Error sending message to {num}: {e}")

    # Wait for the specified delay between messages
    print(f"Waiting for {delay_time} seconds before sending the next message.")
    time.sleep(delay_time)

# Function to send message to all contacts with delay between each message
def send_to_all(message, delay=5):
    for num in contacts.values():
        send_whatsapp_message(num, message, delay)

# Function to display the contact list
def display_contacts():
    print("Select a contact to send the message to:")
    for key, value in contacts.items():
        print(f"{key}. {value}")

# Function to add a new contact
def add_new_contact():
    new_key = str(len(contacts) + 1)  # Create a new unique key
    new_number = input("Enter the new contact number (in international format, e.g., +919XXXXXXXXX): ")
    contacts[new_key] = new_number
    print(f"New contact {new_number} added successfully.")

# Main function
def main():
    while True:
        print("\nSelect an option:")
        print("1. Send message to all contacts")
        print("2. Send message to a particular participant")
        print("3. Add a new contact")
        print("4. Exit")

        option = input("Enter the option number: ")

        if option == '1':
            # Send message to all contacts with a delay of 5 seconds
            message = input("Enter your message: ")
            delay = int(input("Enter the delay (in seconds) between each message: "))
            send_to_all(message, delay)

        elif option == '2':
            # Display contact list and select a particular contact
            display_contacts()
            choice = input("Enter the number of the contact you want to send a message to: ")

            if choice not in contacts:
                print("Invalid choice, please select a valid contact.")
                continue

            # Send message to the selected contact
            message = input("Enter your message: ")
            send_whatsapp_message(contacts[choice], message, 0)  # No delay for individual contact

        elif option == '3':
            # Add a new contact
            add_new_contact()

        elif option == '4':
            # Exit the loop
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please select 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()
