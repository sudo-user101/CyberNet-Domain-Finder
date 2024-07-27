import customtkinter as ck
import requests as r

ck.set_appearance_mode("dark")
ck.set_default_color_theme("blue")

root = ck.CTk()
root.title("CyberNet Labs. Domain Checker")
root.geometry("600x420")

def check_domain_availability(url):
    try:
        status_report = r.get("https://" + url)
        return status_report.status_code == 200
    except r.RequestException:
        return False

def status_checker():
    try:
        user_input = name_of_domain.get()
        domain_dict = {
            "United States": f"{user_input}.com",
            "United Kingdom": f"{user_input}.co.uk",
            "Australia": f"{user_input}.com.au",
            "South Africa": f"{user_input}.co.za",
            "Canada": f"{user_input}.ca",
            "Germany": f"{user_input}.de",
            "France": f"{user_input}.fr",
            "Japan": f"{user_input}.jp",
            "China": f"{user_input}.cn",
            "Brazil": f"{user_input}.com.br",
            "India": f"{user_input}.in",
            "South Korea": f"{user_input}.kr",
            "Mexico": f"{user_input}.mx",
            "Italy": f"{user_input}.it",
            "Netherlands": f"{user_input}.nl",
            "Sweden": f"{user_input}.se",
            "Norway": f"{user_input}.no",
            "Spain": f"{user_input}.es",
            "Poland": f"{user_input}.pl",
            "Switzerland": f"{user_input}.ch",
            "Belgium": f"{user_input}.be",
            "Austria": f"{user_input}.at",
            "Denmark": f"{user_input}.dk",
            "Finland": f"{user_input}.fi",
            "Ireland": f"{user_input}.ie",
            "Portugal": f"{user_input}.pt",
            "Singapore": f"{user_input}.sg",
            "Hong Kong": f"{user_input}.hk"
        }

        value_of_other_regions = False
        list_of_other_regions = []

        for region, domain in domain_dict.items():
            if check_domain_availability(domain):
                if not value_of_other_regions:
                    status.configure(text="Status: Found")
                    type_of_domain.configure(text=f'Domain: {region}')
                    value_of_other_regions = True
                if len(region) > 2:
                    list_of_other_regions.append(region)

        if value_of_other_regions:
            other_regions.configure(text=f"Other Regions: {', '.join(list_of_other_regions)}")
        else:
            status.configure(text="Status: Unavailable")
            type_of_domain.configure(text="Domain: Unknown")
            other_regions.configure(text="Other Regions: None")

    except Exception as e:
        status.configure(text=f"Status: Error - {e}")
        type_of_domain.configure(text="Domain: Unknown")
        other_regions.configure(text="Other Regions: None")

main_frame = ck.CTkFrame(root)
main_frame.pack(pady=15, expand=True, fill="both")

font_size = 18

cyperNetHeader = ck.CTkLabel(main_frame, text="CyberNet Domain Checker", text_color="white", font=("Hack", 23))
cyperNetHeader.grid(row=0, column=0, padx=10, pady=8, sticky='nsew')

status = ck.CTkLabel(main_frame, text="Status: None")
status.grid(row=1, column=0, padx=10, pady=4, sticky='nsew')

type_of_domain = ck.CTkLabel(main_frame, text="Domain: None")
type_of_domain.grid(row=2, column=0, padx=10, pady=4, sticky='nsew')

other_regions = ck.CTkLabel(main_frame, text="Other Regions: None")
other_regions.grid(row=3, column=0, padx=10, pady=4, sticky='nsew')

name_of_domain = ck.CTkEntry(main_frame, text_color="white", font=("Hack", font_size))
name_of_domain.grid(row=5, column=0, padx=10, pady=6, sticky='nsew')

submit_button = ck.CTkButton(main_frame, text="Done", text_color="white", bg_color="#00CED1", font=("Hack", font_size),
                             command=status_checker)
submit_button.grid(row=6, column=0, padx=7, pady=10, sticky='nsew')

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_rowconfigure(4, weight=1)
main_frame.grid_rowconfigure(5, weight=1)
main_frame.grid_rowconfigure(6, weight=1)

root.mainloop()
