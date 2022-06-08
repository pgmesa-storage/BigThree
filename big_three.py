
from datetime import datetime


today = datetime.today()
grand_slams = ["Australian Open", "Roland Garros", "Wimbledon", "US Open"]

class TenisPlayer():
    
    def __init__(self, name:str, last_name:str, birth_date:datetime, nickname:str=None) -> None:
        self.name = name
        self.last_name = last_name
        self.nickname = nickname
        self.birth_date = birth_date
        self.age = self.get_age()
        self.grand_slam_titles = {}
    
    def get_age(self) -> int:
        birthdate = self.birth_date
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def get_full_name(self) -> str:
        return self.name + " " + self.last_name
    
    def set_grand_slams_from_dict(self, info_dict:dict):
        for gs in info_dict:
            if gs not in grand_slams:
                raise ValueError(f"'{gs}' is not a valid Grand Slam -> {grand_slams}")
        self.grand_slam_titles = info_dict
        
    def count_grand_slams(self) -> int:
        count = 0
        for gs in grand_slams:
            num = len(self.grand_slam_titles.get(gs, []))
            count += num
            
        return count
    
    def get_slams_per_year(self, since_year=2000, to_year=today.year, get_years=False, accumulative=True) -> list:
        array = []
        year_range = range(since_year, to_year + 1)
        y_count = 0
        for year in year_range:
            if not accumulative:
                y_count = 0
            for y_array in self.grand_slam_titles.values():
                if year in y_array:
                    y_count += 1
            array.append(y_count)
        
        if get_years:
            return list(year_range), array
        return array
        
    def get_summary_as_list(self, return_headers=False) -> list:
        headers = ["Name", "Last Name", "Age"] + grand_slams + ["Total G-Slams"]
        summary = [self.name, self.last_name, self.age]
        for gs in grand_slams:
            num = len(self.grand_slam_titles.get(gs, []))
            summary.append(num)
        summary.append(self.count_grand_slams())
        
        if return_headers:
            summary = (headers, summary)
        
        return summary
    
    
def get_big_three():
    # Rafa
    rafa = TenisPlayer("Rafael", "Nadal", datetime(1986, 6, 3), nickname="Rafa")
    rafa_slams = {
        "Australian Open": [
            2009, 2022
        ],
        "Roland Garros":[
            2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2017, 2018, 2019, 2020, 2022
        ],
        "Wimbledon": [
            2008, 2010
        ],
        "US Open": [
            2010 ,2013, 2017, 2019
        ]
    }
    rafa.set_grand_slams_from_dict(rafa_slams)
    # Djoko
    djoko = TenisPlayer("Novak", "Djokovic", datetime(1987, 5, 22))
    djoko_slams = {
        "Australian Open": [
            2008, 2011, 2012, 2013, 2015, 2016, 2019, 2020, 2021
        ],
        "Roland Garros":[
            2016, 2021
        ],
        "Wimbledon": [
            2011, 2014, 2015, 2018, 2019, 2021
        ],
        "US Open": [
            2011, 2015, 2018
        ]
    }
    djoko.set_grand_slams_from_dict(djoko_slams)
    # Federer
    federer = TenisPlayer("Roger", "Federer", datetime(1981, 8, 8))
    federer_slams = {
        "Australian Open": [
            2004, 2006, 2007, 2010, 2017, 2018    
        ],
        "Roland Garros":[
            2009
        ],
        "Wimbledon": [
            2003, 2004, 2005, 2006, 2007, 2009, 2012, 2017
        ],
        "US Open": [
            2004, 2005, 2006, 2007, 2008
        ]
    }
    federer.set_grand_slams_from_dict(federer_slams)
    
    return rafa, djoko, federer


if __name__ == "__main__":
    rafa, djoko, federer = get_big_three()
    
    print(rafa.get_slams_per_year())
    
