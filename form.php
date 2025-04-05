<!-- party_form.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Party Planner</title>
</head>
<body>
    <h1>Select Your Party Items</h1>
    <form method="GET" action="run_party_planner.php">
        <?php
        $items = [
            "Cake", "Balloons", "Music System", "Lights", "Catering Service",
            "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
            "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
        ];
        foreach ($items as $index => $item) {
            echo "<label><input type='checkbox' name='items[]' value='$index'> $item</label><br>";
        }
        ?>
        <input type="submit" value="Plan Party">
    </form>
</body>
</html>
