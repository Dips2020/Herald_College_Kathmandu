<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>first php</title>
</head>

<body>

    <?php
    // else if
    // ladder if else
    // if else if
    
    // ⬇️1
    $a = 1000000000000000000;
    $b = 20;
    $c = 5000000;
    echo "Hello <br>";
    if ($a > $b and $a > $c) {
        echo "A: $a is greatest <br>";
    } else if ($b > $a and $b > $c) {
        echo "B: $b is greatest <br>";

    } else if ($c > $a && $c > $b) { // ' and ' or '&&' both works
        echo "C: $c is greatest <br>";
    }


    // ⬇️2
    $a1 = 5000;
    $b1 = 1000;
    $c1 = 20000;
    if ($a1 > $b1) {
        // echo "A: $a1 is greater than $b1 <br>";
        if ($a1 > $c1) {
            echo "A: $a1 is greater than $c1 <br>";
        } else {
            echo "A: $a1 is not greater than $b1 and $c1 <br>";
        }
    } else if ($b1 > $a1) {
        // echo "B: $b1 is grater than $a1 <br>";
        if ($b1 > $c1) {
            echo "B: $b1 is greater than $c1 <br>";
        } else {
            echo "B: $b1 is not greater than $a1 and $c1 <br>";
        }
    } else if ($c1 > $a1) {
        // echo "C: $c1 is grater than $a1 <br>";
        if ($c1 > $b1) {
            echo "C: $c1 is greater than $b1 <br>";
        } else {
            echo "C: $c1 is not greater than $a1 and $b1 <br>";
        }
    }

    // ⬇️3
    // $day = 1;
    $day = "Sunday";
    // $day = 3;
    switch ($day) {
        case "Sunday":
            echo "Sunday";
            break;
        case 2:
            echo "Monday";
            break;

        default:
            echo "Invalid";
            break;
    }
    ?>


</body>

</html>