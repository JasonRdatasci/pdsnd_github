import time
import pandas as pd
import numpy as np
import calendar as cal

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
    while city.lower() not in ["chicago", "new york city", "washington"]:
        print("Sorry, that's not an option. Try again.")
        city = input("Would you like to see data for Chicago, New York City, or Washington?")
    print("Ok, let's check out ", city.title())

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month from the first half of 2017 do you want to see? You can also choose 'all' to see all months.").lower()
    while month.lower() not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("Sorry, that's not an option. Try again.")
        month = input("Which month from the first half of 2017 do you want to see? You can also choose 'all' to see all months.").lower()
    print('Ok, {} it is!'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Finally, which day of the week do you want to see? You can also choose 'all' to see every day.").lower()
    while day.lower() not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
        print("Sorry, that's not an option. Try again.")
        day = input("Finally, which day of the week do you want to see? You can also choose 'all' to see every day.").lower()
    print('Good choice!')

    print('-'*40)
    return city, month, day

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = cal.month_name[df['month'].mode()[0]]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    if popular_hour > 12:
        hour12 = popular_hour - 12
        print("Most common hour is: {}:00 pm".format(hour12))
    else:
         print("Most common hour is: {}:00 am".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df["start end count"] = df["Start Station"]+ " and "+ df["End Station"]
    popular_start_end = (df["start end count"].mode()[0])
    print('Most Common Combination of Start and End Stations:', popular_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds = df["Trip Duration"].sum()
    t=int(total_seconds)
    #https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days/4048773
    day= t//86400
    hour= (t-(day*86400))//3600
    minit= (t - ((day*86400) + (hour*3600)))//60
    seconds= t - ((day*86400) + (hour*3600) + (minit*60))
    print("The total trip duration was {} days, {} hours, {} minutes, {} seconds".format(day, hour, minit, seconds))
    # TO DO: display mean travel time
    mean_seconds = df["Trip Duration"].mean()
    t1 = int(mean_seconds)
    day1 = t1//86400
    hour1 = (t1-(day1*86400))//3600
    minit1 = (t1 - ((day1*86400) + (hour1*3600)))//60
    seconds1 = t1 - ((day1*86400) + (hour1*3600) + (minit1*60))
    print("The average trip duration was {} hours, {} minutes, {} seconds".format( hour1, minit1, seconds1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print("There are {} subscribers and {} customers".format(user_types[0], user_types[1]))

    # TO DO: Display counts of gender
    colnames = list(df)
    if "Gender" not in df:
        print("Sorry, we do not have data on gender for Washington")
    else:
        genders = pd.value_counts(df['Gender'])
        print("There are {} men and {} women".format(genders[0],genders[1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    colnames = list(df)
    if "Birth Year" not in colnames:
        print("Sorry, we do not have data on birth years for Washington")
    else:
        common_year = df["Birth Year"].mode()[0]
        print("The most common birth year is: ", common_year)
        max_year = df["Birth Year"].max()
        print("The most recent birth year is: ", max_year)
        min_year = df["Birth Year"].min()
        print("The oldest birth year is: ", min_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_row_start = 0
        raw_row_end = 5
        data = input("Do you want to see the raw data that generated these metrics? (Yes/No)")
        while True:
            if data.lower() not in ["yes","no"]:
                print("Sorry, try again")
                continue
            elif data.lower() == "yes":
                print(df.iloc[raw_row_start:raw_row_end])
                raw_row_start += 5
                raw_row_end += 5
                data = input("would you like to see five more rows? (Yes/No)")
            elif data.lower() == "no":
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
