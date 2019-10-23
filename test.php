<?php 
 $data=$_POST['data'];//宣告post的變數key是data,value由使用者傳送
 $command='python test.py';
 $command2='python test2.py';
 $command3='python normal_pretreatment2.py';
 $command4='python pretreatment1.py';
 $command5='python mood_analysis.py';
 $command6='python main.py';
 #$command4='python normal_pretreatment.py';
 if($_POST['data']=="title2")
 {
    $output = shell_exec($command);
 }
 else if($_POST['data']=="pro")
 {
   $output = shell_exec($command3);
 }
 else if($_POST['data']=="promood")
 {
   $output = shell_exec($command4);
 }
 else if($_POST['data']=="moodanalysis")
 {
   $output = shell_exec($command5);
 }
 else if($_POST['data'=="textanalysis"])
 {
   $output = shell_exec($command6);
 }
 //echo "data = ".$data;//返回印出data = 使用者傳送key為data的value
?>