<?php

$cmd = 'sudo /sbin/shutdown -h +1';

define('TOKEN', '引っ張ってきたやつ');
define('ACCEPT_TEAM', 'デスクトップからログインして，URLのT00000の部分');
define('ACCEPT_CHANNEL', 'デスクトップからログインして，URLのC00000の部分');

// データが送られてきたことを確認
if (isset($_POST) and !empty($_POST)) {
  // 送信元チェック
  if ($_POST['token'] == TOKEN and $_POST['team_id'] == ACCEPT_TEAM and $_POST['channel_id'] == ACCEPT_CHANNEL) {

    // execではうまくいかなかったので，systemで実行
    $return = system($cmd, $status);

    // ステータスの確認
    if ($status == 0) {
      $text = '1分後にシャットダウンしといてやるよ';
    }
    else {
      $text = '失敗や💢💢💢' . "\n" . '連絡して💢💢💢';
    }

    // データの整形とか
    $channel = '#centos';
    $botname = 'CentOS';
    $emoji = ':smirk_cat:';
    $head = '<@' . $_POST['user_id'] . '|' . $_POST['user_name'] . '> "' . $cmd . '" を実行';
    $message = $head . "\n" . '```' . "\n" . $text . "\n" . '```';

    $payload = [
      'channel' => $channel,
      'username' => $botname,
      'icon_emoji' => $emoji,
      'text' => $message
    ];
    echo json_encode($payload);
  }
}

?>
