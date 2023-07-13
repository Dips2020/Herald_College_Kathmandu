<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>loop php</title>
</head>

<body>

    <?php
    // ⬇️1 for loop
    // for ($i = 0; $i < 10; $i++) {
    
    // }
    
    // ⬇️2 while loop
    // while (){
    
    // }
    
    //⬇️3 do while
    // do{
    
    // }while()
    

    // ⬇️4 foreach applying foreach loop in a array
    $array1 = array(1, 2, 3, 4, 5);
    foreach ($array1 as $value) {
        $value = $value + 1;
        echo "The value of array1 are $value <br>";
    }

    // ⬇️5 for loop in array
    $array2 = array(1, 2, 3, 4, 5);
    for ($i = 0; $i < count($array2); $i++) {
        echo "Value of array at index $i is $array2[$i] <br>";
    }

    // ⬇️6 numeric array
    $array3 = array(1, 2, 3, 4, 5);
    $array3[0] = "Ram";
    // $array3[10] = "Hanuman";
    var_dump($array3);

    ?>

</body>

</html>