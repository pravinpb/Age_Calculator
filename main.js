
function age() {
var birth_date = document.getElementById('date').value;
var birt_month = document.getElementById('month').value;
var birth_year = document.getElementById('year').value;

var date = new Date();
var current_date = date.getDate();
var current_month = 1 + date.getMonth();
var current_year = date.getFullYear();
var month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

if(birth_date == '' || birt_month == '' || birth_year == ''){
    document.getElementById('age').innerHTML = 'Fill the required fields';
} else {

    if(birth_date > current_date){
        current_date = current_date + month_days[current_month-1]
        current_month = current_month -1
    }
    if (birt_month > current_month){
        current_month = current_month +12
        current_year = current_year-1
    }

    var date_age = current_date - birth_date
    var month_age = current_month - birt_month
    var year_age = current_year - birth_year

    document.getElementById('age').innerHTML = 'Your Age is '+year_age+' Years '+month_age+' Months '+date_age+' Days';
}
}