import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}





def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        while True:
            city = input("Which city would you like to filter by? New York City, Chicago or Washington?").title()
            if city in ['Chicago', 'New York City', 'Washington']:
                break
            else:
                print("wrong city")
        while True:
            month = input("nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?").title()
            if month in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
                break
            else:
                print("wrong month")
        while True:
            day = input("nWhich day would you like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.").title()
            if day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','All']:
                break
            else:
                print("wrong day")

    except:
        print("Input Error")

    print('-' * 40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['start hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("the most common month ", common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the most common day of week: ", common_day)

    # display the most common start hour

    common_start_hour = df['start hour'].mode()[0]
    print("the most common start hour ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station ", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station ", common_end_station)
    # display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip ",  group_field[0]," and ",group_field[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("the total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("counts of user types: ", counts_of_user_types)

    # Display counts of gender
    try:
        Counts_of_gender = df['Gender'].value_counts()
        print("counts of gender: ", counts_of_user_types)
    except:
        print("no available data")

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('Most Common Year:', common)
        print('Most Recent Year:', recent)
        print('Earliest Year:', earliest)
    else:
        print("no available data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    display_data(df)

def display_data(df):
    yes_no=['yes','y','no','n']
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no or y or n\n').lower()

    while True:
        if view_data in yes_no:
            break
        else:
            print("please enter yes,no or y,n")


    start_loc = 0
    while view_data == 'yes' or view_data == 'y':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
