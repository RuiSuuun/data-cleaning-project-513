import pandas as pd

from enum import Enum
from pandas import DataFrame
from typing import List


class Event(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"


def get_data():
    # Load a CSV file as a data frame (df) using pandas
    data = pd.read_csv('menu.csv', sep=',')

    # Drop the following columns because all values are NaN
    data = data.drop(columns=['name', 'keywords', 'language', 'location_type', 'place'])
    data = data.rename(columns={'new_place': 'place'})
    return data


def select_sponsor_by_event(event: Event):
    df = get_data()
    sponsors = df.loc[df['event'].str.contains(event.name) == True]
    return sponsors


def select_sponsor_by_locations(locations: List[str]):
    df = get_data()
    sponsors = df.loc[df["place"].isin(locations)]
    return sponsors


def process_result(data: DataFrame):
    # One sponsor can have multiple similar events.
    # This processing steps deduplicate the dataframe.
    data = data.drop(columns=['event'])
    data = data.drop_duplicates(subset=['sponsor'], ignore_index=True)
    return data


def process_result_after_merging(data: DataFrame):
    # Process duplicated columns after merging action.
    duplicated_columns = ['id_y', 'venue_y', 'place_y', 'city/town_y', 'state/country_y', 'physical_description_y',
                          'occasion_y', 'notes_y', 'call_number_y', 'date_y', 'location_y', 'currency_y',
                          'currency_symbol_y', 'status_y', 'page_count_y', 'dish_count_y']
    data = data.drop(columns=duplicated_columns)
    data = data.rename(columns={'id_x': 'id', 'venue_x': 'venue', 'place_x': 'place', 'city/town_x': 'city/town',
                                'state/country_x': 'state/country', 'physical_description_x': 'physical_description',
                                'occasion_x': 'occasion', 'notes_x': 'notes', 'call_number_x': 'call_number',
                                'date_x': 'date', 'location_x': 'location', 'currency_x': 'currency',
                                'currency_symbol_x': 'currency_symbol', 'status_x': 'status',
                                'page_count_x': 'page_count', 'dish_count_x': 'dish_count'})
    return data


def save_result(data: DataFrame, name: str):
    data.to_csv("output/" + name, index=False)


# @BEGIN main
# @PARAM event_name
# @PARAM location
# @IN input_data_file  @URI file: menu.csv
# @OUT sponsors_providing_dinner.csv
# @OUT sponsors_providing_both_breakfast_and_lunch.csv
# @OUT sponsors_in_NYC.csv
def enact():
    """
    Case 1: Which sponsors offer breakfast/lunch/dinner?

    :return: DataFrame
    """
    # Task 1: Select sponsors providing specific event.
    # @BEGIN sponsors_providing_dinner
    # @PARAM event_name
    # @IN g  @AS input_data_file  @URI file: menu.csv
    # @OUT pp  @AS sponsors_providing_dinner.csv
    sponsors_providing_dinner = select_sponsor_by_event(Event.DINNER)
    sponsors_providing_dinner = process_result(sponsors_providing_dinner)
    # print(sponsors_providing_dinner.to_string())
    save_result(sponsors_providing_dinner, "sponsors_providing_dinner.csv")
    print("The total number of sponsors which provides dinner is:", len(sponsors_providing_dinner))
    # @END sponsors_providing_dinner

    # Task 2: Select sponsors providing multiple events simultaneously.
    # @BEGIN sponsors_providing_both_breakfast_and_lunch
    # @PARAM event_name
    # @IN g  @AS input_data_file  @URI file: menu.csv
    # @OUT pp  @AS sponsors_providing_both_breakfast_and_lunch.csv
    sponsors_providing_breakfast = select_sponsor_by_event(Event.BREAKFAST)
    sponsors_providing_breakfast = process_result(sponsors_providing_breakfast)
    print("The total number of sponsors which provides breakfast is:", len(sponsors_providing_breakfast))
    sponsors_providing_lunch = select_sponsor_by_event(Event.LUNCH)
    sponsors_providing_lunch = process_result(sponsors_providing_lunch)
    print("The total number of sponsors which provides lunch is:", len(sponsors_providing_lunch))
    sponsors_providing_both_breakfast_and_lunch = \
        sponsors_providing_breakfast.merge(sponsors_providing_lunch, how='inner', on=["sponsor"])
    sponsors_providing_both_breakfast_and_lunch = \
        process_result_after_merging(sponsors_providing_both_breakfast_and_lunch)
    # print(sponsors_providing_both_breakfast_and_lunch.to_string())
    save_result(sponsors_providing_both_breakfast_and_lunch, "sponsors_providing_both_breakfast_and_lunch.csv")
    print("The total number of sponsors which provides both breakfast and lunch is:",
          len(sponsors_providing_both_breakfast_and_lunch))
    # @END sponsors_providing_both_breakfast_and_lunch

    """
    Case2:  Which sponsors are located in New York, NY?

    :return: DataFrame
    """
    # @BEGIN sponsors_in_NYC
    # @PARAM location
    # @IN g  @AS input_data_file  @URI file: menu.csv
    # @OUT pp  @AS sponsors_in_NYC.csv
    sponsors_in_NYC = select_sponsor_by_locations(["NEW YORK, NY", "NEW YORK,NY", "NEW YORK", "NYC"])
    sponsors_in_NYC = process_result(sponsors_in_NYC)
    # print(sponsors_in_NYC.to_string())
    save_result(sponsors_in_NYC, "sponsors_in_NYC.csv")
    print("The total number of sponsors in New York City is:", len(sponsors_in_NYC))
    # @END sponsors_in_NYC


# @END main


if __name__ == '__main__':
    enact()
