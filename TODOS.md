# Apartments

Default behavior level 1:
create apartment app, model, serialzier
using admin create two apartments
test generic list view

Customize behavior level 2:
Make one property belong to 'admin'
create list veiw (same or multiple) that filters on 'admin'

# Roles and Groups

create groups
create permissions that check user group identity
add these permissions to the views
use permissions in the serializer

# Clearly Defined Goal

The site should allow for multiple 'Admin' users.
Admin users (User.role=='admin') should be able to create Staff users, (User.role=='staff') and assign specific 'Apartment' Objects to them. CRUD Permissions for both 'Admin' and 'Staff' are limited to their properties.

Intuition:
Create Staff -
To create 'Staff' users have a view with '[IsAdmin]' permission that passes data to a 'CreateStaffSerializer' that links new 'Staff' user to the current Admin with 'User.created*by=(self.request.user)' and sets role to 'Staff' with User.role='staff'. Optional parameter that accepts 'Apartment' Objects. Also create a seperate View to assign 'Apartments'.
Apartment Objects will be assigned with a seperate Table 'StaffManagedApartments' that links Staff user to Apartments. A 'StaffManagedApartmentsSerializer' will check if the Apartment Object belongs to the correct 'Admin' via, User.created_by before creating.
To view all 'Apartments' assigned to a Staff user use 'StaffManagedApartments.objects.filter_by(staff_id=user.id)'
To view all Admin's 'Staff' currently managing 'Apartments' use 'StaffManagedApartments.objects.filter_by(admin_id=user.id).group_by(staff_id)'
Example:
class StaffManagedApartments(models.Model):
staff_id = models.ForeignKey(User) # specify in serializer the User.roles and User.created_by checks
admin_id = models.ForeignKey(User)
apartment_id = models.ForeignKey(Apartment)
\*\** unique together (staff*id and apartment_id) *\*\*

class TenantRentedApartments(models.Model):
tennant*id = models.ForeignKey(User)
admin_id = models.ForeignKey(User)
apartment_id = models.ForeignKey(Apartment) # related name ('tennants')
\*\** one tennant = multiple props one prop = multiple tennants \_\*\*
