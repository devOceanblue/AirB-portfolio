from data.Models.WishlistRepository import WishlistRepository


class WishlistService:
    def __init__(self):
        self.repo = WishlistRepository()

    def register_wishlist(self, body=None):
        return self.repo.register_wishlist(body=body)

    def search_user_wishlist(self, user_id):
        return self.repo.search_user_wishlist(user_id)

    def search_wishlist(self, id):
        return self.repo.search_wishlist(id=id)

    def delete_wishlist(self, id):
        return self.repo.delete_wishlist(id=id)

    def create_wishlist(self, user_id, body):
        return self.repo.create_wishlist(user_id, body)
