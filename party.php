<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['items'])) {
    $indices = implode(",", $_POST['items']);
    $command = escapeshellcmd("python3 party_planner.py $indices");
    $output = shell_exec($command);
    echo $output;
} else {
    echo "<h3>No items selected or invalid request.</h3>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Party starter</title>
</head>
<body>
    <h1>Server </h1>
</body>
</html>