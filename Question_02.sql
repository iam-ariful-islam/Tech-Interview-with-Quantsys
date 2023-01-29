/*Question 02

input:
    Donar
    ------------------------------
    Name, Donations, DonationCatID

    DonationCat
    ------------------------------
    DonationCat, Category

ouput:
    Results
    ------------------------------
    Name, Donations, CategoryName
*/


SELECT Donors.Name, Donors.Donations, DonationCat.Category as CategoryName FROM Donor INNER JOIN DonationCat ON Donors.DonationCatID = DonationCat.Id