<?php
    ini_set( 'display_errors', 1 );
ini_set('SMTP','mailhog' );
ini_set('smtp_port',1025);
    error_reporting( E_ALL );
    $from = "danny@danielhanold.com";
    $to = "someonelse@aol.com";
    $subject = "PHP Mail Test script";
    $message = "This is a test to check the PHP Mail functionality";
    $headers = "From:" . $from;
    mail($to,$subject,$message, $headers);
    echo "Test email sent";
