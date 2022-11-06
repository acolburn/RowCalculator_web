import streamlit as st
from datetime import datetime, timedelta


def calculate(str_distance):
    output = ""
    today = datetime.today()
    # today_formatted = today.strftime('%m/%d/%Y')
    end_date = datetime(2023, 5, 1)
    diff = end_date - today
    days_left = diff.days
    weeks_left = days_left / 7
    try:
        dist_rowed = int(str_distance)
    except ValueError:
        return 'Error: Please enter number of meters rowed.'
    else:
        dist_left = 1000000 - dist_rowed
        dist_per_day = round(dist_left / days_left)
        dist_per_week = round(dist_left / weeks_left)
        wks_at_20k_per_week = dist_left / 20000
        end_date_at_20k_per_week = today + timedelta(weeks=wks_at_20k_per_week)
        end_date_at_20k_per_week_formatted = end_date_at_20k_per_week.strftime('%m/%d')
        output += f"Distance rowed: {dist_rowed}\n"
        output += f"Distance left: {dist_left} m\n"
        output += f"Days left: {days_left}\n"
        output += f"{dist_per_week} m per week\n"
        output += f"{round(dist_per_week / 5)} m/day if you row 5X\n"
        output += f"{round(dist_per_week / 6)} m/day if you row 6X\n"
        output += f"{dist_per_day} m/day if you row daily\n"
        output += f"End {end_date_at_20k_per_week_formatted} if you row 20k per week"
        return output


# main
s=''
input_value = st.text_input('Distance: ', value="0")
if st.button('Enter'):
    s = calculate(input_value)
st.text_area('Show results', s, height=300)
