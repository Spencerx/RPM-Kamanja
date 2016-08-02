#!/usr/bin/env bash
input_file=$1
while read hostname
do
   echo "Installing kamanja on $hostname"
   ssh $hostname "rpm -ivh https://s3.amazonaws.com/kamanja/samples/Kamanja-1.5.0_2.11-1.el7.centos.noarch.rpm "
   if [ $? -eq 0 ]; then
    echo "Installation on $hostname successful"
   else
    echo "Installation on $hostname failed"
   fi
done < $input_file
