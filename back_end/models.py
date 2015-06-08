# Create your models here.


class StoreInfo:
    comp_id = None
    store_name = None
    store_name_cn = None
    sub_domain = None
    logo = None
    status = None
    profile = None
    profile_cn = None
    contact = None
    mobile = None
    tel = None
    email = None
    apply_time = None
    online_time = None
    offline_time = None
    create_time = None
    create_by = None
    last_update_time = None
    last_update_by = None

    def __init__(self, comp_id, store_name, store_name_cn, sub_domain, status):
        self.comp_id = comp_id
        self.store_name = store_name
        self.store_name_cn = store_name_cn
        self.sub_domain = sub_domain
        self.status = status

    def to_string(self):
        print("comp_id = %s, store_name = %s, store_name_cn = %s, sub_domain = %s, logo = %s, status = %s, profile = %s, profile_cn = %s, contact = %s, mobile = %s, tel = %s, email = %s, apply_time = %s, online_time = %s, offline_time = %s, create_time = %s, create_by = %s, last_update_time = %s, last_update_by = %s" % (self.comp_id, self.store_name, self.store_name_cn, self.sub_domain, self.logo, self.status, self.profile, self.profile_cn, self.contact, self.mobile, self.tel, self.email, self.apply_time, self.online_time, self.offline_time, self.create_time, self.create_by, self.last_update_time, self.last_update_by))

    def convert_to_dict(self):
        store_info_dict = { '__class__':self.__class__.__name__, '__module__':self.__module__,}
        store_info_dict.update(self.__dict__)
        return store_info_dict