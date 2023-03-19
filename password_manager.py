import sqlite3

class PasswordManager:
    """
    Une classe pour gérer les mots de passe dans une base de données SQLite.
    """

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def add_password(self, website, username, password):
        """
        Ajoute un mot de passe à la base de données.

        Args:
            website (str): Le nom du site pour lequel le mot de passe est utilisé.
            username (str): Le nom d'utilisateur associé au mot de passe.
            password (str): Le mot de passe à stocker.
        """
        self.cursor.execute('INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)', (website, username, password))
        self.conn.commit()

    def get_password(self, website, username):
        """
        Récupère un mot de passe depuis la base de données.

        Args:
            website (str): Le nom du site pour lequel le mot de passe est utilisé.
            username (str): Le nom d'utilisateur associé au mot de passe.

        Returns:
            str: Le mot de passe associé au site web et à l'utilisateur.
        """
        self.cursor.execute('SELECT password FROM passwords WHERE website=? AND username=?', (website, username))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def delete_password(self, website, username):
        """
        Supprime un mot de passe de la base de données.

        Args:
            website (str): Le nom du site pour lequel le mot de passe est utilisé.
            username (str): Le nom d'utilisateur associé au mot de passe.
        """
        self.cursor.execute('DELETE FROM passwords WHERE website=? AND username=?', (website, username))
        self.conn.commit()

    def update_password(self, website, username, password):
        """
        Met à jour un mot de passe dans la base de données.

        Args:
            website (str): Le nom du site pour lequel le mot de passe est utilisé.
            username (str): Le nom d'utilisateur associé au mot de passe.
            password (str): Le nouveau mot de passe à stocker.
        """
        self.cursor.execute('UPDATE passwords SET password=? WHERE website=? AND username=?', (password, website, username))
        self.conn.commit()

    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()
