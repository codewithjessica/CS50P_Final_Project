import PySimpleGUI as psg


def main():

    psg.theme("DarkGrey2")

    provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
                 "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island",
                 "Quebec", "Saskatchewan", "Yukon"]

    layout = [
        [psg.Text("Choose Province"),psg.Combo(provinces, default_value = "Ontario", key = "-PROVINCE-")],
        [psg.Text("Amount $"),psg.Input(key = "-AMOUNT-")],
        [psg.Text("Price Includes Tax?"),psg.Radio("No", "tax", key="-NO-", default=True), \
         psg.Radio("Yes", "tax", key="-YES-")],
        [psg.Button("Calculate", key = "-CALCULATE-")],
        [psg.Text("", key = "-TAX-")],
        [psg.Text("Outcome", key = "-OUTPUT-")],
    ]


    window = psg.Window("Canadian Sales Tax Calculator", layout)

    while True:
        event, values = window.read()

        if event == psg.WIN_CLOSED:
            break
        
        if event == "-CALCULATE-":
            amount = values["-AMOUNT-"]
            province = values["-PROVINCE-"]
            
            if amount.isnumeric() and values["-NO-"] == True:
                window["-TAX-"].update(tax(amount, province)[1]) 
                total = round(without_tax(amount, province),2)
                result = f"${amount} after tax in {province} is ${total}."
                window["-OUTPUT-"].update(result)
            
            elif amount.isnumeric() and values["-YES-"] == True:
                window["-TAX-"].update(tax(amount, province)[1])
                total = round(include_tax(amount, province),2)
                result = f"${amount} before tax in {province} is ${total}."
                window["-OUTPUT-"].update(result)

            else:
                window["-TAX-"].update("")
                error = "Please provide a positive price value."
                window["-OUTPUT-"].update(error)

    window.close()


def tax(amount, province):
    amount = float(amount)

    match province:
        case "Alberta" | "Northwest Territories"| "Nunavut"| "Yukon":
            return 0.05, "GST(5%): $" + str(amount * 0.05)
        
        case "British Columbia" | "Manitoba":
            return 0.12, "GST(7%): $" + str(amount * 0.07) + \
            "    PST(5%): $" + str(amount * 0.05)
        
        case "New Brunswick" | "Newfoundland and Labrador" | "Nova Scotia" | \
            "Prince Edward Island":
            return 0.15, "HST(15%): $" + str(amount * 0.15) 
        
        case "Ontario":
            return 0.13, "HST(13%): $" + str(amount * 0.13) 
        
        case "Quebec":
            return 0.14975, "GST(9.975%): $" + str(amount * 0.09975) + \
            "    QST(5%): $" + str(amount * 0.05)
        
        case "Saskatchewan":
            return 0.11, "GST(6%): $" + str(amount * 0.06) + \
            "    PST(5%): $" + str(amount * 0.05)

    
def without_tax(amount, province):
    amount = float(amount)
    return amount * (1 + tax(amount, province)[0])


def include_tax(amount, province):
    amount = float(amount)
    return amount * (1 - tax(amount, province)[0])


if __name__ == "__main__":
    main()
