<?php
if (isset($_GET['items'])) {
    $selected = $_GET['items'];
    $indices = implode(",", $selected);
    $output = shell_exec("python3 party_planner.py " . escapeshellarg($indices));
    echo $output;
} else {
    echo "<p>No items selected.</p>";
}
?>
