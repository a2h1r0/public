<?php

define('TOKEN', 'なんちゃら');
define('ACCEPT_TEAM', 'なんちゃら');
define('ACCEPT_CHANNEL', 'なんちゃら');

if (isset($_POST) and !empty($_POST)) {
  if ($_POST['token'] == TOKEN and $_POST['team_id'] == ACCEPT_TEAM and $_POST['channel_id'] == ACCEPT_CHANNEL) {
    $text = $_POST['trigger_word'];
    switch ($_POST['trigger_word']) {
      case 'default!':
      $path = '"/var/www/html"';
      break;

      case 'abc!':
      $path = '"/var/www/html/abc"';
      break;

      case 'def!':
      $path = '"/var/www/html/def"';
      break;
    }

    $cp = 'cp /home/ユーザ名/temp/httpd_bk.conf /home/ユーザ名/temp/httpd.conf';
    system($cp, $status);
    if ($status != 0) {
      $text = 'httpdのコピー失敗や💢💢💢';
    } else {

      $echo = "echo 'DocumentRoot " . $path . "' >> /home/ユーザ名/temp/httpd.conf";
      system($echo, $status);
      if ($status != 0) {
        $text = 'httpdへの書き込み失敗や💢💢💢';
      } else {

        $mv = 'sudo mv /home/ユーザ名/temp/httpd.conf /etc/httpd/conf/httpd.conf';
        system($mv, $status);
        if ($status != 0) {
          $text = 'httpdの上書き失敗や💢💢💢';
        } else {

          $restart = 'sudo systemctl restart httpd';
          system($restart, $status);
          if ($status != 0) {
            $text = 'Apacheの再起動失敗や💢💢💢';
          } else {

            # 実行成功時はここで再起動されるため，以下は読まれない #

          }
        }
      }
    }

    # エラー時のみ実行 #
    $channel = '#なんちゃら';
    $botname = 'なんちゃら';
    $emoji = ':smirk_cat:';
    $head = '<@' . $_POST['user_id'] . '|' . $_POST['user_name'] . '> エラー';
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
