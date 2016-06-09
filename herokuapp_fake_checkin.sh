curl -i -X POST -d "hostname=test&datetime=`date --iso-8601=minutes`&head=fakehead&temp=900.1" https://network-observatory.herokuapp.com/post-measurement-box-checkin
