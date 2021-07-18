import time
import pandas as pd
import numpy as np

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
    print('Welcome! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    sdcitychk = True

    while sdcitychk == True :

        city = input("Would you like to see data for Chicago, New York, or Washington? :")
        city = city.lower()

        if city == 'chicago' or city == 'new york' or city == 'washington':
            sdcitychk = False
        else:
            print("Your input is not Chicago, New York, or Washington. Please try again.")

        if city == 'new york':
            city = 'new_york_city'

    # TO DO: get user input for month (all, january, february, ... , june)

    smonthchk = True

    while smonthchk == True :

        month = input("Which month that you would like to see information (January - June)? Type \'all\' if you would like to see data from every month :")
        month = month.title()

        if month == 'All' or month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June':
            smonthchk = False

        else:
            print("Your input is not a valid month name between January and June. Please try again.")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    sdaychk = True

    while sdaychk == True :

        day = input("Which day of week that you would like to see information? Type \'all\' if you would like to see data from everyday :")
        day = day.title()

        if day == 'All' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday':
            sdaychk = False
        else:
            print("Your input is not a valid day of week. Please try again.")



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

    # Load Data Section

    df = pd.read_csv(city + '.csv')


    # Preparation for data filtering

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of week'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour
    df['cnt'] = 1


    # Data Filtering

    if month != 'All':
        df = df[df['Month'] == month]
    if day != 'All':
        df = df[df['Day of week'] == day]


    # Raw Data Preview Section

    prewchk = True

    while prewchk == True :

        prew = input("Would you like to see filtered raw data? Type \'yes\' or \'no\' :")
        prew = prew.title()

        if prew == 'Yes' or prew == 'No':
           prewchk = False

        else:
           print('Invalid input. Please try again')

    if prew == 'Yes':
       i = 0
       while i <= len(df)-1:
             drange=df.iloc[i:min(i+5,len(df)), :-4]
             print(drange)
             i += 5

             contprewchk = True
             while contprewchk == True :
                   contprew = input("Would you like to continue? Type \'yes\' or \'no\' :")
                   contprew = contprew.title()

                   if contprew == 'Yes' or contprew == 'No':
                      contprewchk = False

                   else:
                        print('Invalid input. Please try again')

             if contprew == 'No':
                break


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print('The most frequent month : ' + df['Month'].value_counts().idxmax())

    # TO DO: display the most common day of week

    print('The most frequent day of week : ' + df['Day of week'].value_counts().idxmax())

    # TO DO: display the most common start hour

    print('The most frequent start hour : ' + str(df['Start Hour'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('The most common start station : ' + df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station

    print('The most common end station : ' + df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip


    sdf = df.groupby(['Start Station','End Station'])['cnt'].sum().to_frame('scnt').reset_index()
    sdf = sdf[sdf == sdf.groupby(level=0).transform('max')]
    ss = sdf.sort_values(sdf.columns[2],ascending=False)
    st = ss.head(1)

    print('The most common combibation is :\n Start Station = ' + str(st.iloc[0,0]) + ' \n End Station = ' + str(st.iloc[0,1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total Travel Time : ' + str(df['Trip Duration'].sum()) + str(' seconds'))

    # TO DO: display mean travel time

    print('Mean Travel Time : ' + str(df['Trip Duration'].mean()) + str(' seconds'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('Count of user by type : \n')
    print(df['User Type'].value_counts().to_string())


    # TO DO: Display counts of gender

    while True:
        try:
            print('\nCount of user by gender : \n')
            print(df['Gender'].value_counts().to_string())
            break
        except:
            print('Selected data contains no gender information')
            break

    # TO DO: Display earliest, most recent, and most common year of birth

    while True:
        try:
            print('\nCount of user by birth date : \n')
            print('User\'s earliest year of birth :' + str(int(df['Birth Year'].min())))
            print('User\'s most recent year of birth :' + str(int(df['Birth Year'].max())))
            print('User\'s most common year of birth :' + str(int(df['Birth Year'].mode())))
            break
        except:
            print('Selected data contains no information about user\'s year of birth')
            break





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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
