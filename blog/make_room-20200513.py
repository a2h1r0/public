import random

class MakeRoom:

    def __init__(self):
        self.member = []
        self.error_msg = 'ボイチャに入ってから実行しやがれ:thumbsdown::thumbsdown::thumbsdown:'

    ### メンバー状態の取得 ###
    def set_member(self, ctx):
        # コマンド実行者がVCに入っていることを確認
        author_in = ctx.author.voice
        if author_in is None: 
            return False

        # VC参加かつオンラインのユーザーを取得
        self.member = [member.name for member in author_in.channel.members if str(member.status) == 'online']
        return True

    ### チーム分け ###
    def make_room(self, ctx, capacity, rooms):
        room = []

        # コマンド実行者がVCに入っていなければ終了
        if self.set_member(ctx) is False:
            return self.error_msg

        # 指定された定員の検証
        if capacity <= 0:
            return 'そんな定員むりです:thumbsdown:'
        if capacity > len(self.member):
            capacity = 2

        # チーム数を計算
        room_num = len(self.member) // capacity
        # 定義した部屋数よりチーム数が多ければ，定員を増やして対処
        if room_num > len(rooms):
            room_num = len(rooms)
            capacity = len(self.member) // room_num

        # チーム分けで余るメンバー数を取得
        remain = len(self.member) % capacity

        # メンバーをシャッフル
        random.shuffle(self.member)

        # ユーザーを分割
        for i in range(room_num):
            # 部屋名を代入
            room.append(str(rooms[i]))
            
            # 定員数だけユーザーを追加
            for j in range(capacity):
                room.extend([self.member.pop()])

            # 余るメンバーが存在する場合は更に1人追加
            if remain > 0:
                room.extend([self.member.pop()])
                remain -= 1

    
        return ('\n'.join(room))