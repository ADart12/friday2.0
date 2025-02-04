import mouth
import command
import chatbot
from colorama import Fore,Style,init
from datetime import datetime

#save the history
def save_log(translQuery):
    with open("command_log.txt",'a') as file:
        file.write(translQuery + "\n")

def check_wake_word(translQuery):    #Check from the wake word friday
    return mouth.WAKE_WORD in translQuery

#formate the responses with dynamic value such as time and date
def format_response(response, current_time, current_date):
    if "{time}" in response:
        response = response.replace("{time}", current_time)
    if "{date}" in response:
        response = response.replace("{date}", current_date)
    return response


def main():
    print(Fore.CYAN+"I am Ready sir!")

    #specify the path to your JSON file
    json_file_path = 'D:\\friday2.0\\responses.json'
    responses = chatbot.load_responses(json_file_path)

    while True:
        translQuery = mouth.listen()

        if translQuery:
            # print(f"Mr Bhatt: {translQuery}")
            save_log(translQuery)
            if check_wake_word(translQuery):
                translQuery = translQuery.lower().replace(mouth.WAKE_WORD, "").strip()

                # Execute Command like open chrome
                if command.execute(translQuery):
                    continue

                # AI chatbot responses (offline)
                response = chatbot.get_response(translQuery,responses)
                current_time = datetime.now().strftime("%H:%M")
                current_date = datetime.now().strftime("%d/%m/%Y")
                response = format_response(response, current_time, current_date)
                mouth.speak(response)


            elif "goodbye" in translQuery or "bye" in translQuery:
                mouth.speak(Fore.GREEN + "Goodbye! Have a great day.")
                print("Exiting...")
                break


if __name__ == "__main__":
    main()