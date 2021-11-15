import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would like to see data for Chicago , New York or Washington? \n').lower()
    while (city not in ['chicago','new york','washington']):
        city=input('Try Again,Would like to see data for Chicago , New York or Washington? \n').lower()




    # get user input for month (all, january, february, ... , june)
    month=input('Which month January, February, March, April, May, June or all?\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day Sunday, Monday, Tuesday, Wednesday, Thursday ,Friday or all?\n ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):


        # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[city])
        df.fillna(method = 'ffill', axis = 0)

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df['hour']=df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month:"+str(df['month'].mode()[0])+"\n")

    # display the most common day of week
    print("The most common day of week:"+str(df['day_of_week'].mode()[0])+"\n")

    # display the most common start hour
    print("The most common start hour:"+str(df['hour'].mode()[0])+"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station: "+str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("The most commonly used end station: "+str(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['combination of start_st & end_st']=df['Start Station']+" and "+df['End Station']
    print("The most frequent combination of start station and end station trip: "+str(df['combination of start_st & end_st'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time: "+str(df['Trip Duration'].sum()))

    # display mean travel time
    print("The mean travel time: " + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if (city=='washington'):
          print('Washington does not have Gender and Birth Year columns')
    else:
          print('\nCalculating User Stats...\n')
          # Display counts of user types
          print(df['User Type'].value_counts())
          # Display counts of gender
          print(df['Gender'].value_counts())
          print("The earliest year: "+str(df['Birth Year'].min()))
          print("The recent year: "+str(df['Birth Year'].max()))
          print("The most common year: "+str(df['Birth Year'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while (view_data=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
