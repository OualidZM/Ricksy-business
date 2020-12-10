from src.app import scrapper_target
import pytest


def caracteristicas_nave(page):
    assert(scrapper_target(page)) == ['X11.C_3.0', '2', 'Saturno', '150Picrat', 'F.L.Y.', '1', 'SistemaSolar',
                                      '200Picrat', 'fl_Terra.X05', ' 2', 'SistemaAlfaCentauri', '400Picrat', 'Xx7.C_7.0', ' 1', ...]
