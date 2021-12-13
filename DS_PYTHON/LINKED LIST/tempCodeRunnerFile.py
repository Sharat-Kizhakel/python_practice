     cur = self.head
                self.head = cur.next
                cur.next.prev = None
