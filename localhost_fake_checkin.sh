curl -i -X POST -d "hostname=test&datetime=`date --iso-8601=minutes`&head=fakehead&temp=900.1" http://localhost:5000/post-measurement-box-checkin
