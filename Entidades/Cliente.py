class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__cuentas = []


    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @property
    def cuentas(self):
        return self.__cuentas

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)
        return True

    def numeroDeCuentas(self):
        return len(self.__cuentas)

    def eliminarCuenta(self, numeroDeCuentaAEliminar):
        cuentasNuevo = []
        for cuenta in self.__cuentas:
            if cuenta.numeroCuenta != numeroDeCuentaAEliminar:
                cuentasNuevo.append(cuenta)
        self.__cuentas = cuentasNuevo

    def tieneEsaCuenta(self,numeroCuenta):
        indiceCuenta = None
        i = 0

        for cuenta in self.__cuentas:
            if cuenta.numeroCuenta == numeroCuenta:
                indiceCuenta = i
                break
            i = i + 1
        return indiceCuenta


    def realizarTransferencia(self,numeroCuentaPropia,numeroCuentaExterna,monto,dniPersonaCuentaExterna,banco):

        indiceCuenta=self.tieneEsaCuenta(numeroCuentaPropia)
        if (indiceCuenta is not None):
            if(self.__cuentas[indiceCuenta].dinero>=monto):
                indiceCliente=banco.tieneEseCliente(dniPersonaCuentaExterna)
                if(indiceCliente is not None):
                    personaAPasar:Cliente=banco.clientes[indiceCliente]
                    indiceCuentaExterna=personaAPasar.tieneEsaCuenta(numeroCuentaExterna)
                    if(indiceCuentaExterna is not None):
                        personaAPasar.__cuentas[indiceCuentaExterna].dinero=personaAPasar.__cuentas[indiceCuentaExterna].dinero+monto
                        self.__cuentas[indiceCuenta].dinero=self.__cuentas[indiceCuenta].dinero-monto
                    else:
                        pass ##NO HAY ESA CUENTA EN ESE CLIENTE
                else:
                    pass ## ESE CLIENTE NO EXISTE
            else:
                return False
                #NO TIENE ESE MONTO
        else:
            pass
            #NO ES SU CUENTA

    def __str__(self):
        cadenaInfo=f'CLIENTE: {self.__nombre} {self.__apellidos} , con DNI : {self.__dni}'
        if(self.numeroDeCuentas()>0):
            for cuenta in self.__cuentas:
                cadenaInfo=cadenaInfo+f'\n{cuenta}'
        else:
            cadenaInfo=cadenaInfo+f'\nNO TIENE CUENTAS'
        return cadenaInfo





