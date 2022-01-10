import ReadData as fsData
import numpy as np
import pandas as pd

# Constant
hotels_data = fsData.getHotelsData()

C = hotels_data['rating'].mean()        # C is the mean vote across the whole report.
m = hotels_data['ratingCount'].quantile(0.75)  # m is the minimum votes required to be listed in the chart.

# Filter out all qualified hotels into a new DataFrame
q_hotels = hotels_data.copy().loc[hotels_data['ratingCount'] >= m]

# Function that computes the weighted rating of each hotel
def weighted_rating(x, m=m, C=C):
    v = int(x['ratingCount'])
    R = int(x['rating'])
    return (v/(v+m) * R) + (m/(m+v) * C)


class HotelRecommenderSys(object):
    def __init__(self):
        self.dfHotels =  hotels_data

    # Get recommend hotels based on WEIGHTED RATING
    def get_weighted_rating(self):
        # Define a new feature 'score' and calculate its value with `weighted_rating()`
        q_hotels['score'] = q_hotels.apply(weighted_rating, axis=1)

        #Sort movies based on score calculated above
        result = q_hotels.sort_values('score', ascending=False)

        print(result)
        return result
    
    # Get recommend hotels based on Content-based
    def get_content_based(self):
        df = self.dfHotels

        # Column 
        specs = ['brand_id', 'cpu', 'os', 'ram', 'display', 'display_resolution',
                 'display_screen', 'weight', 'price', 'discount_price']

        # Convert column values to String
        for column in specs:
            df[column] = df[column].apply(str)

        # áp dụng hàm cho mỗi hàng trong khung dữ liệu để lưu trữ các chuỗi được kết hợp vào một cột mới được gọi là combined_specs
        df['combined_specs'] = df.apply(combined_specs, axis=1)

hotel = HotelRecommenderSys()
print(hotel.get_weighted_rating())