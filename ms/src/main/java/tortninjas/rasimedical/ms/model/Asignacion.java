package tortninjas.rasimedical.ms.model;

import java.util.Date;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Getter;
import lombok.Setter;


@Setter
@Getter
@Document(collection = "Asignacion")
public class Asignacion {

    @Id
    public Long id;

    public String tipo;
    
    public Date fecha;

    public Boolean activo;

    public Long elemento;

    public Long medico;

    public Asignacion(String tipo, Date fecha, Boolean activo, Long elemento, Long medico) {
        this.fecha = fecha;
        this.activo = activo;
        this.tipo = tipo;
        this.elemento = elemento;
        this.medico = medico;
    }

    @Override
  public String toString() {
        return "Asignacion[id=" + id + ", tipo=" + tipo + ", fecha=" + fecha
         + ", activo=" + activo + ", elemento=" + elemento + ", medico=" 
         + medico + "]";
  }
  
}
