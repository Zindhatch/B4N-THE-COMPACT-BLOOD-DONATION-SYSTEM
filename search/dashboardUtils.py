import datetime
from dreg .models import DonorList

# returns list of dates when donor donated
def getDonationRecord(donorID):
    result = list()
    try:
        donationDates = DonorList.objects.get(id__iexact = donorID).donation_record.all()
    except:
        return None
    for donationDate in donationDates:
        result.append(str(donationDate.date.date())) #date in YYYY-mm-dd format
    return result

def nextDonationDate(donorID):
    try:
        donationDates = DonorList.objects.get(id__iexact = donorID).last_donate_date
    except:
        return None
    nextDate = donationDates + datetime.timedelta(days=90)  #after 3 months
    return str(nextDate)
    
