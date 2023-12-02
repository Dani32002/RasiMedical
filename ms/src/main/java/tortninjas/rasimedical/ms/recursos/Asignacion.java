package tortninjas.rasimedical.ms.recursos;

import java.util.Date;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;


@Setter
@Getter
@Document(collection = "Asignacion")
@Data
public class Asignacion {

    @Id
    public String id;

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
