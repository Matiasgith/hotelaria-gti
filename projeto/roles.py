from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions ={'listar_hospe': True,'cad_hospe': True,'detalhes_hospe': True,'editar_hospe': True,'del_hospe': True,'listar_quarto': True,'cad_quarto': True,'detalhes_quarto': True,'edit_quarto': True,'del_quarto': True,'oculto_quarto': True,'listar_reserva': True,'cad_reserva': True,'detalhes_reserva': True,'edit_reserva': True,'del_reserva': True,'login_conta': True,'cadastro_conta': True,'logout_conta': True,'edit_conta': True,


    }
class Atendente(AbstractUserRole):
    available_permissions ={'listar_hospe': True,'cad_hospe': True,'detalhes_hospe': True,'editar_hospe': True,'listar_quarto': True,'detalhes_quarto': True,'oculto_quarto': True,'listar_reserva': True,'cad_reserva': True,'detalhes_reserva': True,'edit_reserva': True,'del_reserva': True,'login_conta': True,'logout_conta': True,

    }