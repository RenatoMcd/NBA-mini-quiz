import pytest
from project import val_stat
from project import get_answer
from project import get_players


def test_val_stat():
    assert val_stat("AST") == "AST"
    with pytest.raises(ValueError):
        val_stat("cat")


def test_get_answer():
    assert get_answer(("Kareem Abdul-Jabbar", 38387),("LeBron James", 37062)) == "1"
    assert get_answer(("Moses Malone", 36928),("LeBron James", 37062)) == "2"

def test_get_players():
    assert get_players("AST")[0] and get_players("AST")[1] in [('John Stockton', 15806), ('Jason Kidd', 12091), ('Chris Paul', 10977), ('Steve Nash', 10335), ('Mark Jackson', 10334), ('Magic Johnson', 10141), ('LeBron James', 10045), ('Oscar Robertson', 9887), ('Isiah Thomas', 9061), ('Gary Payton', 8966), ('Russell Westbrook', 8611), ('Andre Miller', 8524), ('Rod Strickland', 7987), ('Rajon Rondo', 7584), ('Maurice Cheeks', 7392), ('Lenny Wilkens', 7211), ('Terry Porter', 7160), ('Tim Hardaway', 7095), ('Tony Parker', 7036), ('Bob Cousy', 6955), ('Guy Rodgers', 6917), ('Deron Williams', 6819), ('Muggsy Bogues', 6726), ('Kevin Johnson', 6711), ('Derek Harper', 6577), ('Nate Archibald', 6476), ('Stephon Marbury', 6471), ('Kyle Lowry', 6469), ('John Lucas', 6454), ('Reggie Theus', 6453), ('James Harden', 6397), ('Norm Nixon', 6386), ('Kobe Bryant', 6306), ('Jerry West', 6238), ('Scottie Pippen', 6135), ('Clyde Drexler', 6125), ('John Havlicek', 6114), ('Baron Davis', 6025), ('Mookie Blaylock', 5972), ('Sam Cassell', 5939), ('Avery Johnson', 5846), ('Nick Van Exel', 5777), ('Dwyane Wade', 5701), ('Larry Bird', 5695), ('Kareem Abdul-Jabbar', 5660), ('Chauncey Billups', 5636), ('Michael Jordan', 5633), ('Allen Iverson', 5624), ('John Wall', 5557), ('Mike Bibby', 5517)]
