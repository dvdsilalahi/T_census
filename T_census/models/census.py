from odoo import api, fields, models, _
from datetime import date

class census_entry(models.Model):

    _name = "census.entry"
    _description = "Census population for Jordan"
    _inherit = ['mail.thread']
    _rec_name = 'id_number'

    name = fields.Char('Name Of Citizen', required=True)
    birth = fields.Date('Date Of birth', default=fields.Date.context_today)
    id_number = fields.Char('ID Number', required=True)
    birth_place = fields.Char('Place Of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'Citizen Gender' ,required=True)
    nationality = fields.Selection([('jordan', 'Jordanian'), ('palestine', 'palestinian'),
                                        ('syria', 'Syrian'), ('iraq', 'Iraqi'),
                                        ('egypt', 'egyption'), ('libya', 'libyan'),
                                        ('yemen', 'yemeni'), ('other', 'other nationality')],
                                   'Citizen Nationality', default='jordan', required=True)
    age = fields.Char('Age', required=True)
    citizen_state = fields.Selection([('retired', 'Retired'), ('working', 'Working'),
                                          ('studying', 'Studying'),('need_job','Searching For A Job'),
                                          ('house_wife', 'A housewife')], 'State Of The Citizen' ,required=True)
    school = fields.Boolean('School')
    school_name = fields.Char('School Name')
    university = fields.Boolean('University')
    university_name = fields.Char('University Name')
    past_job = fields.Char('Past Job')
    your_study = fields.Char('Your Study')
    work = fields.Char('Work')
    bachelor = fields.Boolean('Bachelor')
    work_address = fields.Char('Work Address')
    phone = fields.Char('Phone Number')
    city = fields.Selection([('amman', 'Amman'),('irbid', 'Irbid'),('zarka', 'Zarka'),
                                ('maan', 'Maan'),('tafila', 'Tafila'),('karak', 'Karak'),
                                ('madaba', 'Madaba'),('mafraq', 'Mafraq'),('jerash', 'Jerash'),
                                ('salt', 'Salt'),('ajloun', 'Ajloun'),('aqaba', 'Aqaba')], 'City')
    mother_name = fields.Char('Mother Name')
    father_name = fields.Char('Father Name')
    address = fields.Char('Address')
    street = fields.Char('Street Name')
    status = fields.Boolean('IS Married')
    children = fields.Boolean('Have Children')
    wife_ids = fields.One2many('census.entry', 'id_number', 'Wife')
    child_ids = fields.One2many('census.entry', 'id_number', 'Child')
    fathers_number_related = fields.Many2one('census.entry', string="Father ID")
    mothers_number_related = fields.Many2one('census.entry', string="Mother ID")

    _sql_constraints = [('id_number_unique', 'unique(id_number)', 'This ID number is already used!')]

    @api.onchange('birth')
    def onchange_get_age(self):
        today = date.today()
        now = today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        val = {
                            'age': now
                            }
        return {'value': val}


    
    def onchange_get_mother_name(self,cr,uid,ids,mothers_number_related,context=None):
        if mothers_number_related:
            census = self.pool.get('census.entry').browse(cr, uid, mothers_number_related, context=None)
            return {'value': {'mother_name': census.mother_name,
                              }}
        return True



# This function for dont repeat the id number
#     def on_change_id_number(self, cr, uid, ids, id_number, context=None):
#         if id_number:
#             return {'value': {'email': id_number}}
#         return {}



#     def _department_get(obj, cr, uid, context=None):
#         if context is None:
#             context = {}
#             user_obj =obj.pool.get('res.users').browse(cr,uid,[uid],context=context )
#             if user_obj:
#                 if user_obj.department_id:
#                     return user_obj.department_id.id
#                 else:
#                     raise osv.except_osv(_('Error!'),_('You should belong'))
#         return False














 # if the person gender is male and the person status is married then open new tab in XML for these information:
        #'wife':fields.char('Wife Name'),
        #'wife_nationality':fields.char('Wife Nationality'),
        #'wife_mother_name':fields.char('Mother Name'),
        #'wife_birth_place':fields.char('Place Of Birth For Wife'),
        #'wife_birth':fields.date('Wife Birth Of Date'),
        #'wife_home':fields.boolean('House keeper'),
        #'wife_job':fields.char('Work'),
        
        
            # if there is children open new tab with create button when click  button open customized form for children:
        #'child_name':fields.char('Child Name'),
        #'child_age':fields.char('Child Age'),
        #'child_gender':fields.selection([('male', 'Male'), ('female', 'Female')], 'Gender' ,required=True),
        #'child_birth':fields.date('Child Birth Of Date'), 

