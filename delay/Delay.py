import math
class delay:

        def __init__(self, audio,n,t):
            self.Audio = audio
            self.rep= n
            self.time=t

        def generar(self):
            b=[]
            v=[]
            d=[]
            f=[]
            frames=int(self.time*44100)
            peaklevel = max(abs(self.Audio))
            print peaklevel
            for j in range (0, self.rep):
                b=[]


                valueLevel = (10**(-10/20))*((2**16)/2.0)
                valueAdjust = valueLevel / float(peaklevel)
                #valueAdjust = (2000-(j*(800))) / float(peaklevel)
                print "valueadjust",valueAdjust
                datosAjustados = self.Audio * valueAdjust
                print max(datosAjustados)
                fram=(frames*self.rep+44100)-(44100*j)


                for i in range (frames*j,len(self.Audio)):

                    c=(self.Audio[i]+datosAjustados[i-(frames*j)])
                    b.append(c)
                print "len de audio",len(self.Audio)
                print "Len de b",len(b)

                if len(self.Audio)==len(b):
                        for k in range (0,len(b)):
                            l=b[k]
                            f.append(l)

                elif len(self.Audio)>=len(b):
                        for o in range (0,(len(self.Audio)-len(b))):
                            m=0
                            d.append(m)
                        for o in range (0,len(b)):
                            m=b[o]
                            d.append(m)
                        for o in range (0,len(d)):
                            n=d[o]
                            f.append(n)


            for p in range (0,len(self.Audio)):
                w=f[p]+f[p+len(self.Audio)]+f[p+(2*len(self.Audio))]
                v.append(w)


            return v




